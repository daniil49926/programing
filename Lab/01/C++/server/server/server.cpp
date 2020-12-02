#include <iostream>
#include <cpp_httplib/httplib.h>
#include <nlohmann/json.hpp>
#include <string>
#include <iomanip>
using json = nlohmann::json;
using namespace httplib;


std::string Wether_information() {Client Cli("https://openweathermap.org"); auto answer = Cli.Get("https://api.openweathermap.org/data/2.5/onecall?lat=44.952116&lon=34.102411&lang=ru&units=metric&appid=0083423f4d6d9885477d9ae0b151ab8f");
	if (answer) return answer->body;
}
std::string Time_information() {Client Cli("https://worldtimeapi.org"); auto answer = Cli.Get("http://worldtimeapi.org/api/timezone/Europe/Simferopol");
	if (answer) return answer->body;

}


void main()
{
	json j = json::parse(Wether_information());
	json t = json::parse(Time_information());
	json new__json;
	Server Serv;
	int time = 0;
	
	std::ifstream f("Wid.html");
	std::string str;
	getline(f, str, '\0');
	int new_i;
	new__json.push_back({ {"Temperature", j["hourly"]["temp"]},  {"Weather", j["hourly"]["weather"][0]["description"] } });
	
    new__json.set_content(str, "text/html");

    Serv.listen("localhost", 3000);

}
