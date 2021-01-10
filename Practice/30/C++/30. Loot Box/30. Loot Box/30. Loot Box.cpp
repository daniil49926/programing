#include <iostream>
#include <vector>
#include <map>
#include <ctime>
struct Coin
{
    unsigned int count;
};
struct Weapon
{
    unsigned int dam;
    unsigned int crit;
    unsigned int durab;
};
struct Armor
{
    unsigned int guard;
    unsigned int durab;
};
struct Rune
{
    unsigned int lvl;
    enum class Elem {AIR, FIRE, WATER, EARTH} element;
};
struct Item;
Item generate();
struct Item
{
    enum class ItemType { COIN, RUNE, WEAPON, ARMOR } type;
    union Value { Coin coin; Rune rune; Weapon weapon; Armor armor; } value;
    Item& operator++ () {
        *this = generate();
        return *this;
    }
};
Item GCoin(unsigned int count) {return { Item{Item::ItemType::COIN,Item::Value{.coin = Coin{count}}} };}
Item GRune(Rune::Elem element, unsigned int level) {return { Item{Item::ItemType::RUNE,Item::Value{.rune = Rune{level, element}}} };}
Item GRfire(unsigned int level) {return GRune(Rune::Elem::FIRE, level);}
Item GRwater(unsigned int level) {return GRune(Rune::Elem::WATER, level);}
Item GRearth(unsigned int level) {return GRune(Rune::Elem::EARTH, level);}
Item GRair(unsigned int level) {return GRune(Rune::Elem::AIR, level);}
Item GWeapon(unsigned int damage, unsigned int critical, unsigned int durability) {return { Item{Item::ItemType::WEAPON, Item::Value{.weapon = Weapon{damage, critical, durability}}} };}
Item GArmor(unsigned int guard, unsigned int durability) {return { Item{Item::ItemType::ARMOR, Item::Value{.armor = Armor{guard,durability}}} };}

template<class T, class S>
struct R {
    T first;
    S second;
};
std::vector<R<Item, double>> chance = {{GCoin(1000), 50},{GRair(1), 14},{GRfire(1), 6},{GRwater(1), 13},{GRearth(1), 7},{GRair(5), 1.4},{GRfire(5), 0.6},{GRwater(5), 1.3},{GRearth(5), 0.7},{GRair(10), 0.14},{GRfire(10), 0.06},{GRwater(10), 0.13},{GRearth(10), 0.07},{GArmor(50,100), 2.8},{GWeapon(100,0,100),1.4},{GWeapon(75,50,100),1.4}};
double counter() {
    double sum = 0;
    for (auto& i : chance)
        sum = sum + i.second;
    return sum;
}
std::ostream& operator<<(std::ostream& out, R<Item, double>& chances) {
    out << chances.second << std::endl;
    return out;
}
Item generate() {
    double r = double(rand() % int(counter()));
    double sum = 0;
    for (auto& elem : chance) {
        if (sum > r or r < sum + elem.second) {
            return elem.first;
        }
        sum = sum + elem.second;
    }
    return chance[0].first;
};
std::string q(Rune::Elem& g) {
    switch (g) {
    case Rune::Elem::AIR:
        return "air";
    case Rune::Elem::FIRE:
        return "fire";
    case Rune::Elem::EARTH:
        return "earth";
    case Rune::Elem::WATER:
        return "water";
    }
    return "rune";
}

std::ostream& operator<< (std::ostream& out, Item& item) {
    Item::ItemType& type = item.type;
    switch (type) {
    case Item::ItemType::COIN:
        out << item.value.coin.count << "Gold";
        break;
    case Item::ItemType::RUNE:
        out << "Rune of " << q(item.value.rune.element) << " ";
        out << item.value.rune.lvl << " lvl";
        break;

    case Item::ItemType::WEAPON:
        out << "Damage: " << item.value.weapon.dam << ", crit: " << item.value.weapon.crit;
        out << ", durability: " << item.value.weapon.durab;
        break;

    case Item::ItemType::ARMOR:
        out << "Guard: " << item.value.armor.guard << ", durability: " << item.value.armor.durab;
        break;
    }
    out << std::endl;
    return out;
}
using LootBox = std::vector<Item>;
LootBox generate_lootbox();
LootBox& operator<<(LootBox& vivod, Item item) {
    vivod.push_back(item);
    return vivod;
}
LootBox generate_lootbox() {
    LootBox vivod;
    srand(time(0));
    for (int j; j < 3; j++) {
        vivod << generate();
    }
    return vivod;
}
std::ostream& operator<<(std::ostream& out, LootBox& lootbox) {
    for (auto& elem : lootbox) {
        out << elem << std::endl;
    }
    return out;
}
int main() {
    while (true) {
        std::cout << "Open LOOTBOX?" << std::endl;
        std::string vvod;
        std::cin >> vvod;
        if (vvod == "yes" or vvod == "YES" or vvod == "Yes" or vvod == "y" or vvod == "Y") {
            std::cout << std::endl;
            auto vivod = generate_lootbox();
            std::cout << vivod;
        }
        if (vvod == "no" or vvod == "No" or vvod == "NO" or vvod == "n" or vvod == "N") {
            break;
        }
    }
}