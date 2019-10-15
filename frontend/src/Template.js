import React, { Component, Fragment } from "react";
import { Grid } from "semantic-ui-react";
import axios from "axios";
// import styled from 'styled-components';

import Heading from "./Heading";
import SearchBar from "./SearchBar";
import WordList from "./WordList";

const BASE_URL =
  "http://ec2-15-164-231-243.ap-northeast-2.compute.amazonaws.com:8000";

class Template extends Component {
  constructor(props) {
    super(props);
    this.state = {
      word: "",
      lang: "python",
      wordError: false,
      searchable: false,
      variables: []
    };
  }

  handleInputChange = event => {
    this.setState({
      [event.target.name]: event.target.value
    });
  };

  handleSubmit = event => {
    event.preventDefault();
    const { word, wordError, searchable } = this.state;

    // FIXME: Word validation
    const regExp = /[^가-힣\s]/g;
    if (word === "" || regExp.test(word)) {
      this.setState(prevState => {
        return { wordError: prevState.wordError || true };
      });
      // console.log("완전한 한글이 아니네요.. wordError", wordError);
    } else {
      this.setState(prevState => {
        return { wordError: prevState.wordError && false };
      });
      // console.log("좋아요.. wordError", wordError);
    }

    if (!wordError) {
      this.setState(prevState => {
        return { searchable: prevState.searchable || true };
      });

      // TODO - Search logic, Render WordList
      axios
        .get(`${BASE_URL}/test/${word}/`)
        .then(response => {
          this.setState({
            variables: response.data.variables
          });
          // console.log(this.state.variables);
        })
        .catch(error => {
          // console.log(error);
        });
    } else {
      this.setState(prevState => {
        return { searchable: prevState.searchable && false };
      });
    }

    // console.log("searchable", searchable);
  };

  render() {
    return (
      <Fragment>
        <Heading />
        <Grid centered columns={2}>
          <SearchBar
            word={this.state.word}
            lang={this.state.lang}
            wordError={this.state.wordError}
            onChange={this.handleInputChange}
            onSubmit={this.handleSubmit}
          />
        </Grid>
        {/* FIXME - 검색 결과 반환 시 렌더링 */}
        {this.state.searchable && (
          <Grid centered columns={3}>
            <WordList variables={this.state.variables} lang={this.state.lang} />
          </Grid>
        )}
      </Fragment>
    );
  }
}

export default Template;
