import React, {PropTypes} from "react";
import {connect} from "react-redux";
import {sqlite3} from "sqlite3";
//import dbFile  from "../../../book_db.db";

import {toggleCheck, incNumber, decNumber} from "../actions";

class Home extends React.Component {
  render() {
    const db = new sqlite3.Database('../../../book_db.db');
    db.serialize(function() {

      db.each("SELECT rowid AS id, info FROM book_list", function(err, row) {
        console.log(row.id + ": " + row.info);
      });
    });

    db.close();

    return (
      <div>

        <h3>List of books</h3>
      </div>
    );
  }
}

export default Home;
