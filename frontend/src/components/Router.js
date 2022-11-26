import { Routes, Route } from "react-router-dom";
import Regions from "./pages/Regions";
import Locations from "./pages/Locations";
import Areas from "./pages/Areas";
import Pokemon from "./pages/Pokemon";

export default function Router() {
  return (
    <Routes>
      <Route path="/" element={<Regions />} />
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
