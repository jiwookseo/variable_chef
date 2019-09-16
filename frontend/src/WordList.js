import React from 'react';
import { Grid, Segment, Label } from 'semantic-ui-react';
// import styled from 'styled-components';

import WordItem from './WordItem';

const cases = {
  snake: 'Snake case 🐍',
  pascal: 'Pascal case 🐫',
  camel: 'Camel case 🐪',
}

const langToCase = {
  javascript: 'camel',
  python: 'snake',
  java: '',
  c: '',
  cpp: '',
}

const WordList = (props) => {
  const { variables, lang } = props;
  const caseKey = langToCase[lang];
  const caseName = cases[caseKey];

  return (
    <Grid.Row>
      <Grid.Column>
        <Segment padded raised size='huge'>
          <Label size='large' attached='top left'>{caseName}</Label> {/*{langCase}*/}
          <Segment.Group>
            {variables.map(variable => 
              <WordItem 
                key={variable.id} 
                name={variable[caseKey]}
              />
            )}
          </Segment.Group>
        </Segment>
      </Grid.Column>
    </Grid.Row>
  );
};

export default WordList;