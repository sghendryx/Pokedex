import Card from "@mui/material/Card";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import Grid from "@mui/material/Grid";
import CircularProgress from "@mui/material/CircularProgress";
import Typography from "@mui/material/Typography";
import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import { useQuery } from "react-query";
import { useParams } from "react-router-dom";

export default function Pokemon() {
  const { area_id, area_name } = useParams();
  const { isLoading, error, data } = useQuery(`get${area_id}Pokemon`, () =>
    fetch(`http://127.0.0.1:8000/pokemon/${area_id}`).then((res) => res.json())
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
        {area_name} Pokemon
      </Typography>
      <Grid container rowSpacing={2} columnSpacing={2}>
        {data.pokemon.map((p) => (
          <Grid item xs={2} key={p.name}>
            <Card>
              <CardMedia
                component="img"
                style={{
                  width: "auto",
                }}
                image={p.sprite}
              />
              <CardContent>
                <Typography
                  variant="h5"
                  style={{
                    "text-transform": "capitalize",
                  }}
                >
                  {p.name}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </>
  );
}
