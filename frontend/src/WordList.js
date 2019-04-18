import React from 'react';
import { Card } from 'semantic-ui-react';
// import styled from 'styled-components';

import WordItem from './WordItem';

const WordList = (props) => {
  const { submitted } = props;

  return (
    <Card
      style={{ 
        marginTop: '5em',
        paddingBottom: '3em' 
      }}
    >
      <Card.Content textAlign='left' header='Snake case' />
      <Card.Content textAlign='left'>
        <WordItem name="temporary_variable" like="16"/>
        <WordItem name="temp_var" like="7"/>
        <WordItem name="tmp_vrb" likw="6"/>
      </Card.Content>
    </Card>
  );
};

export default WordList;