describe('template spec', () => {
  it('passes', () => {
    cy.visit('https://the-internet.herokuapp.com/login')
  })
})
describe('E2E Login Negative', () => {

  it('input valid username dan password then Login', () => {

    cy.visit('https://the-internet.herokuapp.com/login')

    cy.get('#username').type("tomsmith")

    cy.get('#password').type("tomsmith")

    cy.get('.fa').click()
  })

})