dir="/home/daipeng/Desktop/program/gblog"

all: ctagsfile etagsfile filenametagsnew cscope
	echo "succuss"

ctagsfile:
	ctags -R -o ctags ${dir}

etagsfile:
	ctags -e -o etags ${dir}

cscope:
	find ${dir} -path ./.git -prune -type f -regex ".*\.\(py\)" -o -print > cscope.files
	cscope -bq

filenametagsnew:
	echo -e "!_TAG_FILE_SORTED\t2\t2/2=foldcase/" > filenametags
	find ${dir} -not -regex '.*\.\(png\|gif\|jpg\|jpeg\|pyc\)' -type f -printf "%f\t%p\t0\n" | grep -v ".git/" | sort -f >> filenametags

ignore:
	cd ${dir}
	touch .gitignore
	echo "ctags" >> .gitignore
	echo "etags" >> .gitignore
	echo "cscope.*" >> .gitignore
	echo "filenametags" >> .gitignore
	echo "makefile" >> .gitignore
	echo "*.log" >> .gitignore
	echo "*.pyc" >> .gitignore
	echo "*.o" >> .gitignore

clean:
	rm -rf ctags etags cscope* filenametags
