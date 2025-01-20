describe('Payment Flow', () => {
  it('should allow a user to complete a payment', () => {
    cy.visit('/login');
    cy.get('input[name="username"]').type('testuser');
    cy.get('input[name="password"]').type('password123');
    cy.get('button[type="submit"]').click();

    cy.url().should('include', '/dashboard');
    cy.visit('/shop');
    cy.get('button[data-test="buy-now"]').first().click();
    cy.get('button[data-test="complete-payment"]').click();

    cy.url().should('include', '/payment-success');
  });
});
