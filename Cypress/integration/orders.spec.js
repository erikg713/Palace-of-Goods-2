describe('Order Placement Tests', () => {
  before(() => {
    cy.request('POST', `${Cypress.env('apiUrl')}/auth/login`, {
      username: Cypress.env('username'),
      password: Cypress.env('password')
    }).then((response) => {
      localStorage.setItem('token', response.body.access_token);
    });
  });

  it('Should allow a user to place an order', () => {
    // Add a product to the cart (assume product ID is 1)
    cy.request({
      method: 'POST',
      url: `${Cypress.env('apiUrl')}/orders`,
      body: {
        product_id: 1,
        quantity: 2
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('order_id');
    });
  });

  it('Should show the order in the user’s order history', () => {
    cy.visit('/orders');
    cy.get('table').find('tr').should('have.length.greaterThan', 1);
  });
});
