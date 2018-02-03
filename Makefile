PY = python
PYFLAGS = 
DOC =
DOCFLAGS = 
DOCCONFIG = config-file

SRC = controller-design/PD-controller-design.py

.PHONY: all prog clean

prog: 
	$(PY) $(PYFLAGS) $(SRC)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

test: 


all: prog doc

clean:
	rm -rf html
	rm -rf latex
