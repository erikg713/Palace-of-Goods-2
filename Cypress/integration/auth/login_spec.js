describe('Login Flow', () => {
  it('should allow a user to log in with valid credentials', () => {
    cy.visit('/login');
    cy.get('input[name="username"]').type('testuser');
    cy.get('input[name="password"]').type('password123');
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/dashboard');
  });

  it('should show an error message with invalid credentials', () => {
    cy.visit('/login');
    cy.get('input[name="username"]').type('invaliduser');
    cy.get('input[name="password"]').type('wrongpassword');
    cy.get('button[type="submit"]').click();
    cy.get('.error-message').should('contain', 'Invalid username or password');
  });
});
