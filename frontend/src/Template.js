import React, { Component, Fragment } from 'react';
import { Grid } from 'semantic-ui-react';
// import styled from 'styled-components';

import Heading from './Heading';
import SearchBar from './SearchBar';
import WordList from './WordList';

class Template extends Component {
  state = {
    word: '',
    lang: '',
    wordError: false,
    submitted: false,
  };

  handleSelectChange = (e, { value }) => {
    this.setState({
      lang: value
    });
    console.log('lang: ', this.state.lang);
  }

  handleInputChange = (e, { value }) => {
    const { word, wordError } = this.state;
    this.setState({
      word: value
    });
    console.log('word: ', this.state.word);

    // Word validation - 완전한 한글 단어인지 체크
    const regExp = /[^가-힣]/g;
    if (word === '' || regExp.test(word)) {
      this.setState({ wordError: true });
      console.log('wordError: ', this.state.wordError);
    } else {
      this.setState({ wordError: false });
      console.log('wordError: ', this.state.wordError);
    }
  }

  handleSubmit = e => {
    e.preventDefault();
    const { word, lang, wordError, submitted } = this.state;

    // FIXME - 제출 시 리스트 렌더링을 위한 submitted
    this.setState({
      submitted: !submitted
    })

    // TODO - 검색 로직
  }

  render() {
    const { 
      word, 
      lang, 
      submitted,
      wordError,
      langError
    } = this.state;

    return (
      <Fragment>
        <Heading/>
        <Grid centered columns={2}>
          <SearchBar 
            word={word}
            lang={lang}
            wordError={wordError}
            langError={langError}
            onChange={this.handleInputChange}
            onSelect={this.handleSelectChange}
            onSubmit={this.handleSubmit}
          />
        </Grid>
        { submitted && 
          <Grid 
            centered 
            columns={3}
          >
            <WordList />
          </Grid>
        }
      </Fragment>
    );
  }
}

export default Template;