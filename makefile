FILES :=                              \
    .travis.yml                       \
    models.html                      \
    IDB1.log                       \
    apiary.apib                     \
    makefile                  \
    models.py                     \
    UML.pdf                   \
    tests.py

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";


status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: Runidb.tmp Testidb.tmp


model.html: models.py
	pydoc -w models

IDB.log:
	git log > IDB1.log

