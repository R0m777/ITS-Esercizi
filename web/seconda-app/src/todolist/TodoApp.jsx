import React, { useEffect, useState } from 'react'
import TodoForm from './TodoForm'
import TodoList from './TodoList'

const API_URL = "http://localhost:3000/"
const TodoApp = () => {
    const [tasks, setTasks] = useState([]);
    const [loading, setloading] = useState(true);
    const [error, setError] = useState(null);

    const fetchTasks = async () => {
        try {
            const response = await fetch(API_URL);
            console.log(response);
            if (!response.ok) throw new Error("Errore nella fetch")

            const data = response.json()
            setTasks(data);
            catch (err)
             }
            setTasks(data);
            catch (err) {

            setError
        }
    };
    useEffect(() => {
        fetchTasks();
    }, []
    );

    return (
        <div>TodoApp
            <TodoForm></TodoForm>
            <TodoList></TodoList>
        </div>
    )
}

export default TodoApp