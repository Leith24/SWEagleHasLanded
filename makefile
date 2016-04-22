FILES :=                              \
    .travis.yml                       \
    models.html                      \
    IDB2.log                       \
    apiary.apib                     \
    makefile                  \
    app/models.py                     \
    UML.pdf                   \
    app/tests.py

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


model.html: app/models.py
	pydoc -w models

IDB.log:
	git log > IDB3.log

