'''def get_file_path(obj, filename):
if hasattr(obj, 'upload_dir'):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join(obj.upload_dir, filename)
else:
    raise AttributeError("%s does not have 'upload_dir' attribute" % obj.__class__.__name__)
	'''
# -*- coding: utf-8 -*-

def m():
	EXT = ('avi', 'mp4')
	filename = 'film.avt'
	extension = filename.split('.')[-1]
	if extension in EXT:
		print u'filename ext in EXT = %s' %extension
	else:
		raise TypeError  

m()		
		
