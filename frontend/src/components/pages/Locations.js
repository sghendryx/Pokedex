import React from "react";
import CircularProgress from "@mui/material/CircularProgress";
import Grid from "@mui/material/Grid";
import Typography from "@mui/material/Typography";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardActionArea from "@mui/material/CardActionArea";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import { useQuery } from "react-query";
import { useNavigate, useParams } from "react-router-dom";

export default function Locations() {
  const { region_id, region_name } = useParams();
  const navigate = useNavigate();
  const { isLoading, error, data } = useQuery(`get${region_id}Locations`, () =>
    fetch(`http://127.0.0.1:8000/locations/${region_id}/`).then((res) =>
      res.json()
    )
  );

  if (isLoading) {
    return <CircularProgress />;
  }
  if (error) {
    return (
      <Alert severity="error">
        <AlertTitle>Error</AlertTitle>
        An error occurred while calling the API
      </Alert>
    );
  }
  return (
    <>
      <Typography variant="h3" mb={4} sx={{ textTransform: "capitalize" }}>
        {region_name} locations
      </Typography>
      <Grid container rowSpacing={2} columnSpacing={2}>
        {data.locations.map(({ name: name, poke_id: location_id }) => (
          <Grid item key={location_id}>
            <Card sx={{ height: "100%", width: 350 }}>
              <CardActionArea
                onClick={() => navigate(`${name}/${location_id}`)}
              >
                <CardContent sx={{ marginLeft: "auto", marginRight: "auto" }}>
                  <Typography
                    variant="h5"
                    sx={{
                      height: 100,
                      textTransform: "capitalize",
                      textAlign: "center",
                    }}
                  >
                    {name}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
}
