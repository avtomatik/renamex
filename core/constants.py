import datetime

LATIN_SUBSTITUTION = '''a,b,v,g,d,e,zh,z,i,y,k,l,m,n,o,p,r,s,t,u,f,kh,ts,ch,sh,shch,,y,,e,yu,ya,,yo'''


MAP_CYRILLIC_TO_LATIN = {
    chr(_): latin for _, latin in enumerate(LATIN_SUBSTITUTION.split(','), start=1072)
}


PREFIXES = {'.', '_', '~'}


FILE_NAME_SRC = 'file_names_d.txt'
FILE_NAME_DST = 'file_names_e.txt'


today = datetime.datetime.today()
formatted_date = today.strftime('%Y-%m-%d_%H-%M-%S')
FILE_NAME_LOG = f'log_{formatted_date}.txt'
