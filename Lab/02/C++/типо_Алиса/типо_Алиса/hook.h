#pragma once

using namespace httplib;
using std::string;
using json = nlohmann::json;

typedef std::vector<string> webhdata;

class Hook {
public:
	int h();
	int poisk(string val);
	void Send(json state, string user_id);
	void Clear(int id);
	string Get(int id);
	void Push(string val);
	void Sav();
	bool Load();
	webhdata data;
	string GetJSON();
	Hook();
private:
	const string filename = "webhooks.json";
	const string field = "WebHooks";
};

Hook webH;

void Hook::Send(json state, string user_id) {
	json fulljson;
	fulljson["user_id"] = user_id;
	fulljson["check"] = state;
	for (int i = 0; i < this->data.size(); i++) {
		string url = this->data.at(i);
		Client cli(url.c_str());
		std::cout << "Post data: " << fulljson << "\n";
		std::cout << "Sending state to " + url + "...";
		std::stringstream ss;
		ss << fulljson;
		auto res = cli.Post("/", ss.str(), "application/json");
		if (res) {
			if (res->status == 200) {
				std::cout << " [OK]\n";
			}
			else {
				std::cout << " [FAIL]\nStatus code: " << res->status << std::endl;
			}
		}
		else {
			std::cout << "[FAIL]\nError code: " << res.error() << std::endl;
		}
	}
}

int Hook::h() {
	return this->data.size();
}

int Hook::poisk(string val) {
	for (int i = 0; i < this->data.size(); i++) {
		if (this->data.at(i) == val) {
			return i;
		}
	}
	return -1;
}

string Hook::GetJSON() {
	json j;
	j["WebHooks"] = json::array();
	for (int i = 0; i < this->data.size(); i++) {
		j["WebHooks"].push_back(this->data[i]);
	}
	std::stringstream ss;
	ss << std::setw(2) << j;
	return ss.str();
}

void Hook::Clear(int id) {
	this->data.erase(this->data.begin() + id);
	this->Sav();
}

string Hook::Get(int id) {
	return this->data.at(id);
}

void Hook::Push(string val) {
	this->data.push_back(val);
	this->Sav();
}

void Hook::Sav() {
	std::ofstream os(this->filename);
	os << this->GetJSON() << std::endl;
	os.close();
}

bool Hook::Load() {
	std::ifstream is(this->filename);
	if (is) {
		json j = json::parse(is);
		for (int i = 0; i < j["WebHooks"].size(); i++) {
			this->data.push_back(j["WebHooks"][i]);
		}
		return true;
	}
	else {
		return false;
	}
	is.close();
}

Hook::Hook() {
	if (!this->Load()) {
		this->Sav();
	}
}