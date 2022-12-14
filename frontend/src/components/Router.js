import { Routes, Route } from "react-router-dom";
import Regions from "./pages/Regions";
import Locations from "./pages/Locations";
import Areas from "./pages/Areas";
import Pokemon from "./pages/Pokemon";
import CreateTeam from "./pages/CreateTeam";

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<Regions />} />
      <Route path="/create-team" element={<CreateTeam />} />
      <Route path="/:region_name/:region_id" element={<Locations />} />
      <Route
        path="/:region_name/:region_id/:location_name/:location_id"
        element={<Areas />}
      />
      <Route
        path="/:region_name/:region_id/:location_name/:location_id/:area_name/:area_id"
        element={<Pokemon />}
      />
    </Routes>
  );
}
