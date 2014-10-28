
import os
import zipfile

zipout  = 'pyreadline-narvi.zip'
ziproot = 'pyreadline-narvi'
licensein = os.path.join('doc', 'COPYING')
licenseout = os.path.join(ziproot, 'pyreadline', 'COPYING')

# get list of files
files = []
for dirpath, dirnames, filenames in os.walk('pyreadline'):
	for f in filenames:
		files.append(os.path.join(dirpath, f))

# create the zip
z = zipfile.ZipFile(zipout, 'w', zipfile.ZIP_DEFLATED)
for f in files:
	z.write(f, os.path.join(ziproot, f))

# add in the license
z.write(licensein, licenseout)

z.close()

