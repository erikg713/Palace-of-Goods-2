describe('Payment Flow', () => {
  beforeEach(() => {
    cy.login('testuser', 'password123'); // Assuming a custom command is created for login
  });

  it('should allow a user to complete a payment', () => {
    cy.visit('/shop');
    cy.get('button[data-test="buy-now"]').first().click();
    cy.get('button[data-test="complete-payment"]').click();
    cy.url().should('include', '/payment-success');
  });

  it('should show an error message if payment fails', () => {
    cy.visit('/shop');
    cy.get('button[data-test="buy-now"]').first().click();
    cy.intercept('POST', '/api/complete-payment', {
      statusCode: 500,
      body: { message: 'Payment failed' },
    });
    cy.get('button[data-test="complete-payment"]').click();
    cy.get('.error-message').should('contain', 'Payment failed');
  });
});
