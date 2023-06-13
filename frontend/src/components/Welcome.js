import { Button, Jumbotron } from 'react-bootstrap';
import React from 'react';

const Welcome = () => (
  <Jumbotron>
    <h1>Images Gallery </h1>
    <p>This is a simple hero unit</p>
    This is simple app that retrives phtots using unsplash api.
    <p>
      <Button varaint="primary" href="https://unsplash.com" target="_blank">
        Learn more
      </Button>
    </p>
  </Jumbotron>
);

export default Welcome;
