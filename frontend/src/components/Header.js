import React from 'react';
import { Navbar, Container } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';
const navbarStyle = {
  backgroundColor: 'lightblue',
};

const Header = (props) => {
  return (
    <Navbar style={navbarStyle} expand="lg">
      <Container>
        <Logo alt={props} style={{ maxWidth: '12rem', maxHeught: '2rem' }} />
      </Container>
    </Navbar>
  );
};

export default Header;
