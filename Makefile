TARGETS	=all clean clobber diff distclean import install uninstall
TARGET	=all

SUBDIRS	=

.PHONY:	${TARGETS} ${SUBDIRS}

PREFIX	=/opt
BINDIR	=${PREFIX}/bin

all::	sort-top.py

check::	sort-top.py
	top -n 1 | python sort-top.py

${TARGETS}::

distclean clobber:: clean

install:: sort-top.py
	install -D sort-top.py ${BINDIR}/sort-top

uninstall::
	${RM} ${BINDIR}/sort-top
