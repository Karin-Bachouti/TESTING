const table = document.createElement('table');
table.border = '1';

function makeEditable(cell) {
  if (cell.querySelector('input')) return;

  const currentText = cell.textContent;
  cell.textContent = '';

  const input = document.createElement('input');
  input.type = 'text';
  input.value = currentText;
  input.className = 'cell-input';
  cell.appendChild(input);
  input.focus();
  input.select();

  function commit() {
    const val = input.value;
    cell.textContent = val === '' ? '' : val;
  }

  input.addEventListener('blur', commit);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') input.blur();
    if (e.key === 'Escape') {
      input.value = currentText;
      input.blur();
    }
  });
}

for (let i = 0; i < 7; i++) {
  const row = table.insertRow();
  for (let j = 0; j < 5; j++) {
    const cell = row.insertCell();
    cell.textContent = `Row ${i + 1}, Col ${j + 1}`;
    cell.addEventListener('click', () => makeEditable(cell));
  }
}

document.body.appendChild(table);
