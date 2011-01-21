import urllib
import string

def get_courses():
	url = 'http://www.vestibular.ufrgs.br/cv2011/DENSIDADE_2011.HTM'
	sock = urllib.urlopen(url)
	courses = []
	for line in sock.readlines():
		line = line.decode('windows-1252').encode('utf-8')
		if line[:3] == '<B>' and line[5].isdigit():
			courses.append(line.split('  ')[1].strip())
	return courses

def get_people(course_name, letter):
	#url = 'http://www.ufrgs.br/coperse/cv2010/listao/CV2010_%s.htm' % letter
	url = 'http://www.ufrgs.br/CVResultados/listao/CV2011_%s.htm' % letter
	people = []
	sock = urllib.urlopen(url)
	for line in sock.readlines():
		line = line.decode('windows-1252').encode('utf-8')
		line = line.replace('*',' ')
		if line.split('  ')[-1].strip() == course_name:
			people.append(" ".join(line.split('  ')[0].split()[6:]))
	return people
