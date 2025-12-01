// manage a list of <li>Item</li> entries using three controls
document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');
  // support either id="my_list" or class="my_list" to match the examples
  const list = document.querySelector('#my_list') || document.querySelector('.my_list');

  if (!list) {
    return;
  }

  if (addItem) {
    addItem.addEventListener('click', () => {
      const li = document.createElement('li');
      li.textContent = 'Item';
      list.appendChild(li);
    });
  }

  if (removeItem) {
    removeItem.addEventListener('click', () => {
      const last = list.lastElementChild;
      if (last) {
        list.removeChild(last);
      }
    });
  }

  if (clearList) {
    clearList.addEventListener('click', () => {
      list.innerHTML = '';
    });
  }
});
