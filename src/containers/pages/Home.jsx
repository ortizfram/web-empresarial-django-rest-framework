import FullWithLayout from "hocs/layouts/FullWithLayout";
import { connect } from "react-redux";
import React from "react";
import { Link } from "react-router-dom";
import WantDemo from 'components/home/WantDemo'
import Header from "components/home/Header";

function Home({}) {
  return (
    <FullWithLayout>
      <Header />
      <WantDemo />
    </FullWithLayout>
  );
}

const mapStateToProps = (state) => ({});

export default connect(mapStateToProps, {})(Home);
