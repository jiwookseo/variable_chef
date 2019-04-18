import React from 'react';
import { Grid, Segment, Label } from 'semantic-ui-react';
// import styled from 'styled-components';

import WordItem from './WordItem';

const WordList = (props) => {
  const { langCase } = props;
  return (
    <Grid.Row>
      <Grid.Column>
        <Segment padded raised size="huge">
          <Label size='large' attached='top left'>Snake case 🐍</Label> {/*{langCase}*/}
          <Segment.Group>
            <WordItem name="temporary_variable" like="16"/>
            <WordItem name="temp_var" like="7"/>
            <WordItem name="tmp_vrb" like="6"/>
          </Segment.Group>
        </Segment>
      </Grid.Column>
    </Grid.Row>
  );
};

export default WordList;