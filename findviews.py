'''
Created on 1 jul 2013

@author: emalinn
'''
import argparse
import subprocess
import re
import datetime


def execute_command(command, return_exitcode=False):
    """
    This function will execute a given command and return the stdout
    information.

    If return_exitcode is True, return a tuple: (returcode, stdoutdata)
    """
#    logging.debug("Executing command " + repr(command))
    command_handle = subprocess.Popen(command,
                                      stdout=subprocess.PIPE)

    (stdoutdata, stderrdata) = command_handle.communicate()

    if stdoutdata is not None:
        stdoutdata = str(stdoutdata, "utf-8")

    if stderrdata is not None:
        stderrdata = str(stderrdata, "utf-8")

    returncode = command_handle.returncode

#    logging.debug("Exit code was " + str(returncode))
#    logging.debug("Stdout was " + str(stdoutdata))
#    logging.debug("Stderr was " + str(stderrdata))

    if return_exitcode:
        return (returncode, stdoutdata)

    else:
        if returncode != 0:
            err_msg = ("Could not execute command '{0}'. \n" +
                       "Output was {1}\n Stderr was {2} \n Exit status: {3}")
            raise ValueError(err_msg.format(' '.join(command),
                                            stdoutdata,
                                            stderrdata,
                                            returncode))

        return stdoutdata



def get_content_from_file(file_path):
    '''
    Read the contents of a file to a string
    :param file_path: The file to read from
    '''
    with open(file_path, 'r') as file_handle:
        return file_handle.read()



def cleartool_lsview_bscauto():
    p1 = subprocess.Popen(['cleartool', 'lsview'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', 'bscauto'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output, err = p2.communicate()
#    p1_returncode = p1.returncode
#    p2_returncode = p2.returncode
#
#    if p1_returncode != 0 or p2_returncode != 0:
#        raise ValueError('Could not fetch all views: {}'.format(err))
    result = str(output, "utf-8")
    return result


def get_all_views(filter_regexp):
    result = cleartool_lsview_bscauto()
#    result = get_content_from_file('/home/emalinn/temp/bscauto_views')

    lines = result.split("\n")
    name_pattern = None
    if filter_regexp is not None:
        name_pattern = re.compile(filter_regexp)
    pattern = re.compile(r'.\s*(\S+)\s+(\S+)')
    view_paths = list()
    for line in lines:
#        print(line)
#        view_path = line.strip().split(' ')[1]
#        view_paths.append(view_path)

        matcher = pattern.search(line)
        if matcher is not None:
            if name_pattern is not None:
                name_matcher = name_pattern.search(matcher.group(1))
                if name_matcher is None:
                    continue
            view_paths.append(matcher.group(2))

    return view_paths


def main():

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-d", "--days",
                            type=int,
                            dest='days',
                            help="Regard all view older than num days",
                            required=False)
    arg_parser.add_argument("-f", "--filter-regexp",
                            type=str,
                            dest='filter_regexp',
                            help="Filter view names with this regexp",
                            required=False)
    args = arg_parser.parse_args()
    num_days = 35
    if args.days is not None:
        num_days = args.days

    view_paths = get_all_views(args.filter_regexp)

    failures = list()
    pattern = re.compile(r'(?P<view_name>.+)\nLast accessed (?P<age>\S+) by (?P<user>[^\.]+)')
    timeout_delta = datetime.timedelta(days=num_days)
    cc_command_temp = 'cleartool setview -exec "cleartool lsp -co -s | xargs cleartool unco -rm " {0} ; yes no | cleartool rmview -tag {0}'
    for view_path in view_paths:
        command = ['cleartool','lsview','-s', '-age', '-storage', view_path]
#        print('Executing: {}'.format(' '.join(command)))
        (return_code, output) = execute_command(command,True)
        if return_code != 0:
            failures.append(view_path)
            continue
        matcher = pattern.search(output)
        if matcher is not None:
            #Clearcase has ':' in its timezone get rid of it
            python_time = ''.join(matcher.group('age').rsplit(':',1))

            age = datetime.datetime.strptime(python_time,"%Y-%m-%dT%H:%M:%S%z")
            if (age + timeout_delta).replace(tzinfo=None) < datetime.datetime.now():
                cc_command = cc_command_temp.format(matcher.group('view_name'))
                print('echo "{} by {}"; {}'.format(age.strftime('%Y-%m-%d'),
                                                   matcher.group('user'),
                                                   cc_command
                                           ))
                
    print('Failures:\n{}'.format("\n".join(failures)))




if __name__ == '__main__':
    exit(main())
