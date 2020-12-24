#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <Windows.h>
#include <time.h> 
struct Student {
	std::string name;
	int group;
	std::map<std::string, int> exams;
};

template<typename T>
bool isSorted(std::vector<T> sort, bool order) {
	if (sort.size() <= 1)
		return true;
	for (int i = 1; i < sort.size(); i++) {
		if (order) {
			if (sort[i] < sort[i - 1]) {
				return false;
			}
		}
		else {
			if (sort[i] > sort[i - 1]) {
				return false;
			}
		}
	}
	return true;
}
int sort_proc1;
int sort_proc2;
template<typename T>
std::vector<T> BozoSort(std::vector<T> sort, bool order = true) {
	srand(time(NULL));
	while (!isSorted(sort, order)) {
		int sort_proc1 = rand() % sort.size();
		int sort_proc2 = rand() % sort.size();
		std::swap(sort[sort_proc1], sort[sort_proc2]);
	}
	return sort;
}

bool operator<(Student jj, Student ii) {
	return jj.name < ii.name;
}
bool operator>(Student jj, Student ii) {
	return jj.name > ii.name;
}
std::string border() {
	return "+--------------+--------+------+------+------+------+""\n";
}

std::string values(std::string contents, int limit) {
	if (contents.length() > limit - 2) {
		contents = contents.substr(0, max(0, limit - 4));
		contents = contents + "..";
	}
	return "| " + contents + std::string(max(0, limit - contents.length() - 1), ' ');
}
std::string head = border() + values("Name", 14) + values("Group", 8) + values("Math", 6) + values("Phys", 6) + values("Hist", 6) + values("Prog", 6) + "|\n";
std::string header() {
	return head;
}
std::string table(Student numb) {
	std::string yyyi = border() + values(numb.name, 14) + values(std::to_string(numb.group), 8) + values(std::to_string(numb.exams["math"]), 6) + values(std::to_string(numb.exams["phys"]), 6) + values(std::to_string(numb.exams["hist"]), 6) + values(std::to_string(numb.exams["prog"]), 6) + "|\n";
	return yyyi;
}
std::ostream& operator<<(std::ostream& new_numb, Student numb) {
	new_numb << header() << table(numb) << border();
	return new_numb;
}

std::ostream& operator<<(std::ostream& new_numb, std::vector<Student> numb) {
	new_numb << header();
	for (int i = 0; i < numb.size(); i++) {
		new_numb << table(numb[i]);
	}
	new_numb << border();
	return new_numb;
}

void main() {
	std::vector<Student> vec = {{ "Vitto S", 2,   { {"math", 4}, {"phys", 3},{"hist", 3}, {"prog", 2} }},
								{ "Henri T", 2,   { {"math", 5}, {"phys", 4},{"hist", 2}, {"prog", 5} }},
								{ "Djo B", 2,     { {"math", 2}, {"phys", 5},{"hist", 5}, {"prog", 5} }},
								{ "Leo G", 2,     { {"math", 3}, {"phys", 5},{"hist", 4}, {"prog", 3} }},
								{ "Karlo F", 2,   { {"math", 5}, {"phys", 5},{"hist", 5}, {"prog", 5} }},
								{ "Frank V", 2,   { {"math", 3}, {"phys", 2},{"hist", 3}, {"prog", 5} }},
								{ "Giuseppe P", 2,{ {"math", 4}, {"phys", 4},{"hist", 4}, {"prog", 4} }},
								{ "Kristina K", 2,{ {"math", 2}, {"phys", 2},{"hist", 2}, {"prog", 2} }},
								{ "Lucco G", 2,   { {"math", 5}, {"phys", 3},{"hist", 4}, {"prog", 3} }},
								{ "Maik B", 2,    { {"math", 5}, {"phys", 3},{"hist", 4}, {"prog", 2} }}
	};
	std::vector<Student> dvoiki;
	for (int i = 0; i < 10; i++) {
		if ((vec[i].exams["math"] == 2) || (vec[i].exams["phys"] == 2) ||
			(vec[i].exams["hist"] == 2) || (vec[i].exams["prog"] == 2)) {
			dvoiki.push_back(vec[i]);
		}
	}

	std::cout << BozoSort(dvoiki) << std::endl;
	std::cout << "Expulsion" << "\n\n";
	srand(time(NULL));
	if (dvoiki.size() > 0) {
		std::cout << dvoiki[rand() % dvoiki.size()];
	}
	else {
		std::cout << "Not found";
	}
}