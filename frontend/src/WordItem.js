import React, { Fragment } from 'react';
import { Header } from 'semantic-ui-react';
// import styled from 'styled-components';

const WordItem = (props) => {
  const { name, like } = props;
  return (
    <Fragment>
      <Header as='h3'>{name}</Header>
      <Header as='h4'>{like}</Header>
    </Fragment>
  );
};


export default WordItem;