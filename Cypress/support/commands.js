Cypress.Commands.add('login', (username, password) => {
  cy.request('POST', `${Cypress.env('apiUrl')}/auth/login`, {
    username,
    password
  }).then((response) => {
    localStorage.setItem('token', response.body.access_token);
  });
});

Cypress.Commands.add('addProduct', (name, description, price) => {
  cy.request({
    method: 'POST',
    url: `${Cypress.env('apiUrl')}/products`,
    body: { name, description, price },
    headers: {
      Authorization: `Bearer ${localStorage.getItem('token')}`
    }
  });
});
before(() => {
  cy.login('testuser', 'testpassword');
  cy.addProduct('Sample Product', 'This is a test product', 100);
});
