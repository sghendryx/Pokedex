import * as React from "react";
import { useNavigate } from "react-router-dom";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ListSubheader from "@mui/material/ListSubheader";
import CatchingPokemonIcon from "@mui/icons-material/CatchingPokemon";
import AssignmentIcon from "@mui/icons-material/Assignment";

export function MainListItems() {
  const navigate = useNavigate();
  return (
    <React.Fragment>
      <ListItemButton onClick={() => navigate("/", { replace: true })}>
        <ListItemIcon>
          <CatchingPokemonIcon />
        </ListItemIcon>
        <ListItemText primary="Regions" />
      </ListItemButton>
    </React.Fragment>
  );
}

export function SecondaryListItems() {
  const navigate = useNavigate();
  return (
    <React.Fragment>
      <ListSubheader component="div" inset>
        Set Team
      </ListSubheader>
      <ListItemButton
        onClick={() => navigate("/create-team", { replace: true })}
      >
        <ListItemIcon>
          <AssignmentIcon />
        </ListItemIcon>
        <ListItemText primary="team name" />
      </ListItemButton>
    </React.Fragment>
  );
}
