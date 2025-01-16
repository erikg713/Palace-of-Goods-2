// File: contracts/Marketplace.sol
pragma solidity ^0.8.0;

contract Marketplace {
    struct Item {
        uint256 id;
        string name;
        uint256 price;
        address owner;
    }

    mapping(uint256 => Item) public items;
    uint256 public itemCount;

    function listItem(string memory _name, uint256 _price) public {
        itemCount++;
        items[itemCount] = Item(itemCount, _name, _price, msg.sender);
    }

    function purchaseItem(uint256 _id) public payable {
        Item storage item = items[_id];
        require(msg.value == item.price, "Incorrect payment amount");
        payable(item.owner).transfer(msg.value);
        item.owner = msg.sender;
    }
}
