#pragma once

#include "Gps.h"

class BusGps : public Gps<BusGps>
{
public:
	BusGps();
	~BusGps();

	void findDestination();

private:
};

#include <iostream>

BusGps::BusGps()
{
}

BusGps::~BusGps()
{
}

void BusGps::findDestination()
{
	std::cout << "Bus destination" << std::endl;
}
