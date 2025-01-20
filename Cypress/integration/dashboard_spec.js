describe('Palace of Goods - Dashboard', () => {
  it('should display the user dashboard after login', () => {
    cy.fixture('testUser').then(user => {
      cy.visit('/login');
      cy.get('input[name="username"]').type(user.username);
      cy.get('input[name="password"]').type(user.password);
      cy.get('button[type="submit"]').click();
    });
    cy.url().should('include', '/dashboard');
    cy.get('.dashboard-welcome').should('contain', 'Welcome, testuser');
  });
});
