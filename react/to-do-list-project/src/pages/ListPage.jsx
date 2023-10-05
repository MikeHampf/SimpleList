import { useContext, useEffect, useState } from "react";
import axios from "axios";
import { api } from "../utilities";

export default function ListPage() {
  console.log(localStorage.id);
  let token = localStorage.token;
  const [list, setList] = useState([]);
  const [item, setItem] = useState("");
  const [notes, setNotes] = useState("");
  const [refetchList, setRefetchList] = useState(true);

  const markDone = async (id) => {
    //event.preventDefault()
    console.log(id);
    let response = await api.put(`/items/update/${id}`, {
      complete: true,
    });
    console.log(response.data);
    setRefetchList(true);
  };

  const markUndone = async (id) => {
    //event.preventDefault()
    console.log(id);
    let response = await api.put(`/items/update/${id}`, {
      complete: false,
    });
    console.log(response.data);
    setRefetchList(true);
  };

  const addItem = async (event) => {
    console.log("ADDING");
    //event.preventDefault()
    if (item) {
      let response = await api.post("items/add/", {
        item: item,
        notes: notes,
      });
      console.log(response.data);
      setItem("");
      setNotes("");
    }
    setRefetchList(true);
  };

  const removeItem = async (id) => {
    console.log("REMOVING");
    let response = await api.delete(`items/delete/${id}`);
    console.log(response.data);
    setRefetchList(true);
  };

  useEffect(() => {
    if (refetchList) {
      axios
        .get("http://127.0.0.1:8000/api/v1/items/", {
          headers: { Authorization: `token ${token}` },
        })
        .then((response) => {
          setList(response.data.to_do_items);
        })
        .finally(() => {
          setRefetchList(false);
        });
    }
  }, [refetchList]); //use the variable, not the set function

  console.log(list);

  return (
    <div className="listPage">
      <h2>YOUR TO DO ITEMS</h2>
      <ul>
        {list.map((item, index) => (
          <div key={index} className="listing">
            <li>{item.entry.date_added}</li>
            <li>{item.entry.item}</li>
            <li>{item.entry.notes}</li>
            <li>{item.entry.complete.toString()}</li>
            <button
              onClick={(event) => {
                markDone(item.id);
              }}
            >
              DONE!
            </button>
            <button
              onClick={(event) => {
                markUndone(item.id);
              }}
            >
              UNDONE!
            </button>
            <button
              onClick={(event) => {
                removeItem(item.id);
              }}
            >
              TOSS IT
            </button>
          </div>
        ))}
        <div className="addListing">
          <input
            className="item"
            placeholder="item *REQUIRED"
            type="text"
            value={item}
            onChange={(event) => setItem(event.target.value)}
          ></input>
          <input
            className="notes"
            placeholder="details"
            value={notes}
            onChange={(event) => setNotes(event.target.value)}
          ></input>
          <button
            onClick={(event) => {
              addItem();
            }}
          >
            ADD IT!
          </button>
        </div>
      </ul>
    </div>
  );
}
