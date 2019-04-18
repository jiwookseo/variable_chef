import React, { Component, Fragment } from 'react';
import { Grid } from 'semantic-ui-react';
import axios from 'axios';
// import styled from 'styled-components';

import Heading from './Heading';
import SearchBar from './SearchBar';
import WordList from './WordList';

class Template extends Component {
  constructor(props) {
    super(props);
    this.state = {
      word: '',
      lang: '',
      wordError: false,
      searchable: false,
      response: {},
    };
  }

  handleSelectChange = (e, { value }) => {
    this.setState({
      lang: value
    });
  }

  handleInputChange = (e, { value }) => {
    this.setState({
      word: value
    });
  }

  handleSubmit = e => {
    e.preventDefault();
    const { word, wordError, searchable } = this.state;

    // FIXME: Word validation
    const regExp = /[^가-힣\s]/g;
    if (word === '' || regExp.test(word)) {
      this.setState((prevState) => { 
        return { wordError: prevState.wordError || true } 
      });
      console.log('완전한 한글이 아니네요.. wordError', wordError);
    } else {
      this.setState((prevState) => { 
        return { wordError: prevState.wordError && false } 
      });
      console.log('좋아요.. wordError', wordError);
    }

    if (!wordError) {
      this.setState((prevState) => {
        return { searchable: prevState.searchable || true }
      })

      // TODO - Search logic, Render WordList
      // axios test
      axios.get('https://dog.ceo/api/breeds/image/random')
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });

    } else {
      this.setState((prevState) => {
        return { searchable: prevState.searchable && false }
      })
    }
    console.log('searchable', searchable);

  }

  render() {
    const { 
      word, 
      lang,
      wordError,
      searchable,
    } = this.state;

    return (
      <Fragment>
        <Heading/>
        <Grid centered columns={2}>
          <SearchBar 
            word={word}
            lang={lang}
            wordError={wordError}
            onChange={this.handleInputChange}
            onSelect={this.handleSelectChange}
            onSubmit={this.handleSubmit}
          />
        </Grid>
        {/* FIXME - 검색 결과 반환 시 렌더링 */}
        { searchable && 
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