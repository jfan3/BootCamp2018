#######################################################################	
all: pi.cpp.exec hidido.cpp.exec quad.cpp.exec monte_carlo.cpp.exec
#######################################################################	

pi.cpp.exec : pi.cpp
	g++ pi.cpp -o pi.cpp.exec
hidido.cpp.exec : name.cpp
	g++ name.cpp -o hidido.cpp.exec
quad.cpp.exec : quad.cpp
	g++ quad.cpp -o quad.cpp.exec
monte_carlo.cpp.exec : monte_carlo.cpp
	g++ monte_carlo.cpp -std=c++11 -o monte_carlo.cpp.exec
#######################################################################	
	
clean :
	rm -f *.exec
