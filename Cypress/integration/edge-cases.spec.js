describe('Edge Case Tests', () => {
  it('Should handle an empty product list', () => {
    cy.request('DELETE', `${Cypress.env('apiUrl')}/products/all`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    }).then(() => {
      cy.visit('/products');
      cy.contains('No products available').should('exist');
    });
  });

  it('Should handle large orders gracefully', () => {
    cy.request({
      method: 'POST',
      url: `${Cypress.env('apiUrl')}/orders`,
      body: {
        product_id: 1,
        quantity: 1000000
      },
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    }).then((response) => {
      expect(response.status).to.eq(400);
      expect(response.body).to.have.property('error', 'Quantity exceeds stock availability');
    });
  });
});
