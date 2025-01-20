describe('Error Handling Tests', () => {
  it('Should show an error message for invalid login', () => {
    cy.visit('/login');
    cy.get('input[placeholder="Username"]').type('wronguser');
    cy.get('input[placeholder="Password"]').type('wrongpass');
    cy.get('button[type="submit"]').click();

    cy.contains('Invalid credentials').should('exist');
  });

  it('Should handle 404 errors gracefully', () => {
    cy.visit('/non-existent-page', { failOnStatusCode: false });
    cy.contains('Page Not Found').should('exist');
  });
});
