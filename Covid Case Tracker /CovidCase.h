#ifndef COVIDCASE_H
#define COVIDCASE_H

#include <iostream>
#include <string>
#include <cmath>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>

using std::vector;
using std::ostream;
using std::string;
using std::cout;
using std::endl;
using std::stod;
using std::stoi;



// TODO: your code  goes here
class CovidCase {
private:

  double latitude;
  double longitude;
  string name;
  int age;
  int time;

public:
   CovidCase(double latitudeIn, double longitudeIn, const string & nameIn, const int ageIn, int timeIn)
        : latitude(latitudeIn), longitude(longitudeIn), name(nameIn), age(ageIn), time(timeIn) {}


  CovidCase( string value){

    std::istringstream iss(value);
    vector<string> tokens;
    copy(std::istream_iterator<string>(iss), std::istream_iterator<string>(),back_inserter(tokens));

    double latitudeIn = stod(tokens[0]);
    double longitudeIn = stod(tokens[1]);
    string nameIn = tokens[2];
    int ageIn = stoi(tokens[3]);

    nameIn.pop_back();
    nameIn.erase(nameIn.begin());
    nameIn.pop_back();

    int timeIn = stoi(tokens[4]);

    latitude = latitudeIn;
    longitude = longitudeIn;
    name = nameIn;
    age = ageIn;
    time = timeIn;
  }

    const double & getLatitude() const{
      return latitude;
    }

    const double & getLongitude() const{
      return longitude;
    }

    const string & getName() const{
      return name;
    }

    const int & getAge() const{
      return age;
    }

    const int & getTime() const{
      return time;
    }

    const double distanceTo(CovidCase other) const{

      double dlon2 = other.getLongitude() ;
      double dlat2 = other.getLatitude();

      double dlong = (dlon2 - longitude) * M_PI/180;
      double dlatt = (dlat2 - latitude) * M_PI/180;

      double a = pow((sin(dlatt/2)), 2) + cos(dlatt) * cos(dlat2) * pow((sin(dlong/2)), 2);
      double c = 2 * atan2( sqrt(a), sqrt(1-a) );
      double d = 3960 * c;
      return d;
    }

    bool operator==(const CovidCase & other) const{

        if ( latitude == other.latitude){
          return true;
        }
        if ( longitude == other.longitude){
          return true;
        }
        if ( name == other.name){
          return true;
        }
        if ( age == other.age){
          return true;
        }
        if ( time == other.time){
          return true;
        }
        else{
          return false;
        }
    }
    bool operator!=(const CovidCase & other) const{

        if ( latitude != other.latitude){
          return true;
        }
        if ( longitude != other.longitude){
          return true;
        }
        if ( name != other.name){
          return true;
        }
        if ( age != other.age){
          return true;
        }
        if ( time != other.time){
          return true;
        }
        else{
          return false;
        }
    }
};

ostream & operator<< (ostream & o, const CovidCase & toPrint){
  o << "{"<< toPrint.getLatitude()<< ", "<< toPrint.getLongitude()<<", "<<'"'<<toPrint.getName()<<'"'<<", "<< toPrint.getAge()<< ", "<< toPrint.getTime()<< "}";
  return o;
}
// don't write any code below this line

#endif
// TODO: Replace this file with your CovidCase.h from Part1
// then extend as per the instructions in README.md
