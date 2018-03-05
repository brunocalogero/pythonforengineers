'''Learn to communicate with other programs

    echo $USER   -->  ['echo', os.environ['USER']]
    echo ~/a.txt 

'''

from subprocess import Popen, PIPE, check_output
import os

def graphviz(dot='digraph {raymond -> matthew;}'):
    p = Popen(['dot', '-Tsvg'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    text, err = p.communicate(input=dot)
    #      ^-- stderr
    # ^------- stdout
    if err:
        return '', err
    svg_start = text.index('<svg')
    svg = text[svg_start:]
    return svg, err

def run_command(cmd):
    if not os.system(cmd + '> tmp.txt'):
        raise RuntimeError('Command failed')
    with open('tmp.txt') as f:
        s = f.read()
    os.remove('tmp.txt')
    return s

if __name__ == '__main__':
    #print run_command('netstat -s').upper()
    #print run_command('ping -c 3 www.cisco.com').upper()

    print check_output('netstat -s', shell=True).upper()
    print check_output(['netstat', '-s']).upper()
    print check_output(['echo', os.environ['USER']])                    # echo $USER
    print check_output(['echo', os.path.expanduser('~/a.txt')])         # echo ~/a.txt
    s = check_output(['ping', '-c', '3', 'www.cisco.com'])
    ping_result = s.splitlines()[-2]
    assert '0.0%' in ping_result.split()

    p = Popen(['sort'], stdin=PIPE, stdout=PIPE, stderr=PIPE)           # cat __doc__ | sort > text
    text, err = p.communicate(input=__doc__)
    print text

    p = Popen(['grep', 'echo'], stdin=PIPE, stdout=PIPE, stderr=PIPE)   # cat __doc__ | grep echo > text
    text, err = p.communicate(input=__doc__)
    print text.upper()

    print graphviz()
