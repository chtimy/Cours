#include <iostream>
#include "TypeName.h"

template<typename T>
void passByValue(T value)
{
	std::cout << "passByValue : " << type_name<decltype(value)>() << std::endl;
}

template<typename T>
void passByRefValue(T& value)
{
	std::cout << "passByRefValue : " << type_name<decltype(value)>() << std::endl;
}

template<typename T>
void passByConstValue(const T value)
{
	std::cout << "passByConstValue : " << type_name<decltype(value)>() << std::endl;
}

template<typename T>
void passByConstRefValue(const T& value)
{
	std::cout << "passByConstRefValue : " << type_name<decltype(value)>() << std::endl;
}

template<typename T>
void passByPtrValue(T* value)
{
	std::cout << "passByPtrValue : " << type_name<decltype(value)>() << std::endl;
}

template<typename T>
void passByConstPtrValue(const T* value)
{
	std::cout << "passByConstPtrValue : " << type_name<decltype(value)>() << std::endl;
}

template<typename T>
void passByConstPtrConstValue(const T* const value)
{
	std::cout << "passByConstPtrConstValue : " << type_name<decltype(value)>() << std::endl;
}

int main()
{
	int x = 5;
	int& rx = x;
	const int& cx = x;
	int* px = &x;
	const int* cpx = &x;
	const int* const cpcx = &x;

	// By value
	// if the expr is a reference, ignore the reference part
	// if after removing the reference, there is a const, ignore also the const
	passByValue(x);
	passByValue(rx);
	passByValue(cx);
	passByValue(px);
	passByValue(cpx);
	passByValue(cpcx);

	passByConstValue(x);
	passByConstValue(rx);
	passByConstValue(cx);
	passByConstValue(px);
	passByConstValue(cpx);
	passByConstValue(cpcx);

	// By reference or by ptr
	// if the expr is a reference, ignore the reference part
	passByRefValue(x);
	passByRefValue(rx);
	passByRefValue(cx);
	passByRefValue(px);
	passByRefValue(cpx);
	passByRefValue(cpcx);

	passByConstRefValue(x);
	passByConstRefValue(rx);
	passByConstRefValue(cx);
	passByConstRefValue(px);
	passByConstRefValue(cpx);
	passByConstRefValue(cpcx);

	passByPtrValue(&x);
	passByPtrValue(&rx);
	passByPtrValue(&cx);
	passByPtrValue(px);
	passByPtrValue(cpx);
	passByPtrValue(cpcx);

	passByConstPtrValue(&x);
	passByConstPtrValue(&rx);
	passByConstPtrValue(&cx);
	passByConstPtrValue(px);
	passByConstPtrValue(cpx);
	passByConstPtrValue(cpcx);

	passByConstPtrConstValue(&x);
	passByConstPtrConstValue(&rx);
	passByConstPtrConstValue(&cx);
	passByConstPtrConstValue(px);
	passByConstPtrConstValue(cpx);
	passByConstPtrConstValue(cpcx);
}