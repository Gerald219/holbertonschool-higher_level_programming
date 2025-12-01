// add a new <li>Item</li> to the .my_list list when #add_item is clicked
const addItem = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

if (addItem && myList) {
  addItem.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });
}
