all :
	python3 CreateLattice.py > CreateLattice.dot
	dot -Tpdf CreateLattice.dot -o Lattice.pdf
	dot -Tpng CreateLattice.dot -o Lattice.png
