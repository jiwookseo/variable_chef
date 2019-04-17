import React from 'react';
import { Card } from 'semantic-ui-react';
// import styled from 'styled-components';

import WordItem from './WordItem';

const WordList = () => {
  return (
    <Card>
      <Card.Content header='Snake case' />
      <Card.Content>
        <WordItem name="temporary_variable" like="16"/>
        <WordItem name="temp_var" like="7"/>
        <WordItem name="tmp_vrb" likw="5"/>
      </Card.Content>
    </Card>
  );
};

export default WordList;