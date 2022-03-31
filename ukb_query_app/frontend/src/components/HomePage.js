import React, { Component } from 'react';
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from 'react-router-dom';

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <Router>
                <Switch>
                    <Route path='/hmpg'>
                        <p>This is the homepage</p>
                        </Route>
                    <Route path='/join'element={RoomJoinPage}></Route>
                    <Route path='/create'element={CreateRoomPage}></Route>
                </Switch>
            </Router>
        )
            
    }
}