#ifndef COVIDCASEMAP_H
#define COVIDCASEMAP_H

#include "CovidCase.h"
#include <vector>
#include <algorithm>
#include <map>

using std::pair;
using std::vector;
using std::map;

// TODO: your code goes here
class TimeAndCaseData {

public:
  int timePositive = 0;
  int activeCases = 0;
  TimeAndCaseData(const int & timeIn)
    : timePositive(timeIn){}

     int getTime(){
      return timePositive;}

    int & getNumberOfCases(){
      return activeCases;}
  };

  bool compare(TimeAndCaseData other, TimeAndCaseData other2){ //for get cases over time
    return other.getTime() < other2.getTime();
  }
  bool compareName(CovidCase other, CovidCase other2){   //for supportVisitGreedyTSP
    return other.getName() < other2.getName();
  }
  bool compareTime(CovidCase other, CovidCase other2){   //for supportVisitGreedyTSP
    return other2.getTime() < other.getTime();
  }

class CovidCaseMap{
private:
  vector <CovidCase> cases;

public:
  void addCase(const CovidCase & other){
    cases.push_back(other);}

  bool searchVector(vector<TimeAndCaseData> other, int value){ //for get cases over time
    for (int i = 0; i < other.size(); i++){
      if (other[i].getTime() == value){return true;}
    }
    return false;}

  vector<TimeAndCaseData> getCasesOverTime(const int & activeTime){

    vector<TimeAndCaseData> active;
    active.push_back(0);

    for(int i = 0; i < cases.size(); i++){
      if ( activeTime > cases[i].getTime()){
        active.push_back(cases[i].getTime());
        active.push_back(cases[i].getTime()+activeTime);
      }
      else if(activeTime < cases[i].getTime()){
        active.push_back(cases[i].getTime());
        active.push_back(cases[i].getTime()+activeTime);
      }
    }

    std::sort(active.begin(),active.end(), compare);

    for(int i = 1; i < active.size(); i++){
          if (!(searchVector(active, active[i].getTime() - activeTime))){
              active[i].getNumberOfCases() = active[i-1].getNumberOfCases() + 1 ;
          }
          else{
                active[i].getNumberOfCases() = active[i-1].getNumberOfCases() - 1 ;
              }
      }
    return active;
  }

  double supportVisitGreedyTSP(const double & latitudeIn, const double & longitudeIn, const int & time, const int & selfiso){
    CovidCase Visit(latitudeIn,longitudeIn, " ",0 ,0);
    vector<CovidCase> activeCases;
    for (int i = 0; i < cases.size(); i++){
      if ( cases[i].getTime() < time){
        activeCases.emplace_back(cases[i]);
      }
    }
      vector<double> minDist;
      double counter= 0;
      double minDistance = 0;
      int s = 0;
      vector<pair<CovidCase,bool>> visited;

      for( int i = 0; i < activeCases.size(); i++){
        visited.emplace_back(activeCases[i],false);
        double distance = Visit.distanceTo(activeCases[i]);
        minDist.emplace_back(distance);
      }
      sort(minDist.begin(), minDist.end());
      counter = minDist.front();
      minDistance = counter;
      minDist.clear();

      int size = activeCases.size();
      int remainder = size % 2;

      if (remainder == 0){
        sort(activeCases.begin(),activeCases.end(),compareTime);
      }
      else{
        sort(activeCases.begin(),activeCases.end(),compareName);
      }

    while ( s < activeCases.size()){

      for ( int i = 0; i < activeCases.size(); i++){
        if ( counter == Visit.distanceTo(visited[i].first)){
              for(int k = 0; k <activeCases.size(); k++){
                double dis = visited[i].first.distanceTo(visited[k].first);
                if (dis != 0){
                minDist.emplace_back(dis);}
              }
              visited[i].second = true;
              }
          }

          for (int i = 0; i < activeCases.size(); i++){ 
            CovidCase c = visited[i].first;
            bool t = visited[i].second;
            for ( int k = 0; k <activeCases.size(); k++){
              double dCheck = c.distanceTo(visited[k].first);
              if ( counter == dCheck){
                visited[k].second = true;
                if ( s == size - 1){
                  double lastTrip = visited[k].first.distanceTo(Visit);
                  minDistance = minDistance + lastTrip;
                }
                for (int a = 0; a < activeCases.size(); a++){
                  if ( visited[a].second != true){
                  double dis = visited[k].first.distanceTo(visited[a].first);
                  if ( dis != 0){
                  minDist.emplace_back(dis);}
                  }
                }
              }
            }
          }

      sort(minDist.begin(), minDist.end());
      if (minDist.size() != 0){
        counter = minDist.front();
        minDistance = minDistance + counter;
      }
      else {
        counter = 0;
        minDistance = minDistance + 0;}


      minDist.clear();
      s++;

    }

    return minDistance;
  }
};
// don't write any code below this line

#endif
